# Social Distancing device

<h3 align="center">
<img src="https://github.com/chandbud5/Social_Distancing_device/blob/main/imgs/Device.png"><br>
Wearable device</h3>

Now a days everyone is worried about **COVID-19**. There are so many people who need to go out in these tough times to earn money. While doing their daily job people need to be cautious and keep social distance from each other.Sometimes while working a person may forget about these things and violate the social distance. As a result they need to face the consequences. Which can lead to loss of many lives.<br><br>

So we have came up with a **simple solution** which can save many lives. We have made an *Arduino* based social distancing device.

<h2>Working</h2>
An *Ultrasonic Sensor* is configured with Arduino. Using this sensor we measure the distance of the user wearing this device and another person. If the distance is *less than* the required distance then the user will get an **Alert message** on their phone. After sending an alert message system will store the timestamp to the *database*. This data can be accessed from a web based potal where user can get statistics about their alerts along with timestamp. So using *web portal* the user can track their device activity.
