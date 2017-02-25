IMAGE_TAG ?= registry.heroku.com/ridindirtyatl-api/web

.DEFAULT: test

.PHONY: build
build:
	docker build -t ${IMAGE_TAG} .

.PHONY: test
test: build test-only

.PHONY: test-only
test-only:
	docker run --rm -it ${IMAGE_TAG} pytest

.PHONY: deploy
ifeq (${TRAVIS_PULL_REQUEST},false)
ifeq (${TRAVIS_BRANCH},master)
deploy:
	wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
	heroku plugins:install heroku-container-registry
	heroku container:login
	docker push ${IMAGE_TAG}
else
deploy:
	@echo "Travis won't deploy when branch is not master"
endif
else
deploy:
	@echo "Travis won't deploy during pull requests"
endif
