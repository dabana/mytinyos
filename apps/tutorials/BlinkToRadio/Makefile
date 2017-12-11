COMPONENT=BlinkToRadioAppC
BUILD_EXTRA_DEPS=BlinkToRadioMsg.class BlinkToRadioMsg.py

BlinkToRadioMsg.class: BlinkToRadioMsg.java
	javac BlinkToRadioMsg.java

BlinkToRadioMsg.java:
	mig java -target=null -java-classname=BlinkToRadioMsg BlinkToRadio.h BlinkToRadioMsg -o $@

BlinkToRadioMsg.py: BlinkToRadio.h
	mig python -target=null -python-classname=BlinkToRadioMsg BlinkToRadio.h BlinkToRadioMsg -o $@


include $(MAKERULES)


