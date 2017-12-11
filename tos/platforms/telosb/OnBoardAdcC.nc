/*
 * This software is a modification of the VoltageC.nc code
 * to be able to use the on board sensors of the TelosB
 * platform (and TelosA). 

 * Here are the different sensors available available through

 *   Msp430InternalVoltageC = Internal voltage reference of
 *   the microcontroller (default sensor of VoltageC) and access to
 *   the ADC via the Msp430InternalVoltageP component (change the inch variable)
 *   located in the tunoys/tos/chips/msp430/sensors folder

 *   Msp430InternalTemperatureC = Internal temperature sensor
 *   of the microcontroller

 *   HamamatsuS1087ParC = On board photodiode with green filter
 *   (sensitivity peak at 550 nm)

 *   HamamatsuS10871TsrC = On board photodiode with no filter
 *   (sensitivity peak at 950 nm)

 *   SensirionSht11C = On board temperature and humidity sensors
 *   can be read at once but values a sent sequentially. Use the .Temperature
 *   method to read temperature and the .Humidity method to read humidity.

 *   
 *
 * Author: David Banville
 * Date: 04-04-2017
 */

generic configuration OnBoardAdcC() {
  provides interface Read<uint16_t>;
}
implementation {
  components new Msp430InternalVoltageC();

  Read = Msp430InternalVoltageC.Read;
}

