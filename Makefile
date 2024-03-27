build: 
	jupyter-book build notebooks/
cleanbuild: clean
	jupyter-book build notebooks/
clean:
	-rm -rf notebooks/_build/

current_dir = $(shell pwd)

shell:
	docker run -it -p 9994:9994 -v $(shell pwd):/book -w /book --platform linux/x86_64 --entrypoint=bash $(DOCKER_USERNAME)/statsthinking21

#	docker run --platform linux/x86_64 -p 9994:9994 -it --entrypoint=bash -v $(current_dir):/analysis poldrack/statsthinking21
