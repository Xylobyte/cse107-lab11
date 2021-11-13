COURSE = cse107
GROUP_NAME = donovan_griego
ASSIGNMENT = lab11
TARGETS = scorehist.py scorebar.py readscores.py actsat.txt README.md design
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)
	@echo "\n--- zip archive created ---\n"
	zipinfo $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip