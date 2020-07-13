build: 
	jupyter-book build notebooks/
cleanbuild: clean
	jupyter-book build notebooks/
clean:
	-rm -rf notebooks/_build/
