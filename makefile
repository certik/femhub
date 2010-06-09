all:
	./femhub -b

clean:
	rm -rf spkg/build

distclean: clean
	rm -rf local
	rm -rf spkg/installed/*
