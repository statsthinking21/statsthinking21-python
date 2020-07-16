build: 
	jupyter-book build notebooks/
cleanbuild: clean
	jupyter-book build notebooks/
clean:
	-rm -rf notebooks/_build/

current_dir = $(shell pwd)

shell:
	docker run -p 9994:9994 -it --entrypoint=bash -v $(current_dir):/analysis poldrack/jupyter-python-r