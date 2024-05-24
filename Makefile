all:
	python -m pip install -vvv -e .
clean:
	-rm -r build hitomi.cpp *.so *.egg-info
