// uses this library: https://github.com/fdebrabander/Arduino-LiquidCrystal-I2C-library
// SCL to A5 on the Arduino
// SDA to A4 on the Arduino
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 4);

void setup()
{
  // initialize the LCD
  lcd.begin();

  // Turn on the blacklight
  lcd.setBacklight((uint8_t)1);

  // First row
  lcd.print("Merry Christmas");

  // Second row
  lcd.setCursor(0,1);
  lcd.print("+");
}

void loop()
{
  // Do nothing here...
}

