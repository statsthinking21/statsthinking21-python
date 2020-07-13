build:
	jupyter-book -W build notebooks/
clean:
	-rm -rf notebooks/_build/
