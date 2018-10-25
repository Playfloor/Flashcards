
cards:
	python ./go.py

clean:
	rm -f *.aux *.log cards.pdf counts mid.pdf mid1.pdf

all:
	for i in *tex; do \
	   	if [ $$i != tikzlibrarycd.code.tex ]; then \
			pdflatex $$i; \
		fi; done;

