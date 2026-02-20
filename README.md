# Ex03 Places Around Me
## Date:10/2/2026

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google as an image.

### STEP 3
Insert the image using ```<img>``` tag and link it to the map.

### STEP 4
Using ```<map>``` tag name the map.

### STEP 5
Create clickable regions in the image using ```<area>``` tag.

### STEP 6
Write HTML programs for all the regions identified.

### STEP 7
Execute the programs and publish them.

## CODE
```
<html>
    <head>
        <title>Map Finder</title>
    </head>
    <body bgcolor="orange">
        <center>
        <h1>Dharshan sanjay .d</h1>
        <h1>212225040070</h1> 
        <h1>velachery chennai</h1>
        <img src="Screenshot 2026-02-10 100246.png" usemap="#image-map">
        <map name="image-map">
        <area target="" alt="Grand Palace" title="Grand Palace" href="grandpalace.html" coords="913,533,1099,600" shape="rect">
        <area target="" alt="Charminar Biriyani" title="Charminar Biriyani" href="Charminar.html" coords="1355,819,1587,854" shape="rect">
        <area target="" alt="puzhithivakam lake" title="puzhithivakam lake" href="lake.html" coords="565,341,557,486,569,629,670,506,660,325" shape="poly">
        <area target="" alt="Nakshatra hotel" title="Nakshatra hotel" href="Nakshatra.html" coords="1103,676,82" shape="circle">
        <area target="" alt="The chennai silks" title="The chennai silks" href="chennaisilks.html" coords="1535,347,85" shape="circle">
        </map>
        </center>
    </body>
</html>

charminar.html
<html>
    <head>
        <title>Charminar Biriyani</title>
    </head>
    <body bgcolor="RED" text="YELLOW" >
        <center>
        <h1>Charminar Biriyani </h1>
        <p1>Famous biriyani shop,created newly in this location</p1>
        </center>
    </body>
</html>

chennaisilks.html
<html>
    <head>
        <title>The Chennai Silks</title>
    </head>
    <body bgcolor="WHITE" text="BLUE" >
        <center>
        <h1>The Chennai Silks</h1>
        <p1>This is the biggest store in our area , where we can get all cloths and jewels</p1>
        </center>
    </body>
</html>

grandpalace.html
<html>
    <head>
        <title>Grand palace</title>
    </head>
    <body bgcolor="LIGHT PINK" text="BLUE" >
        <center>
        <h1>Grand palace</h1>
        <p1>This is the biggest store in our area</p1>
        </center>
    </body>
</html>

lake.html
<html>
    <head>
        <title>Grand palace</title>
    </head>
    <body bgcolor="LIGHT PINK" text="BLUE" >
        <center>
        <h1>Grand palace</h1>
        <p1>This is the biggest store in our area</p1>
        </center>
    </body>
</html>

Nakshatra.html
<html>
    <head>
        <title>Nakshatra Pure VEG</title>
    </head>
    <body bgcolor="TEAL" text="BLACK" >
        <center>
        <h1>Nakshatra Pure VEG</h1>
        <p1>This is famoys well known shop for vegetarians</p1>
        </center>
    </body>
</html>

```

## OUTPUT
![alt text](<Screenshot (16).png>) ![alt text](<Screenshot (17).png>) ![alt text](<Screenshot (18).png>) ![alt text](<Screenshot (19).png>) ![alt text](<Screenshot (20).png>) ![alt text](<Screenshot (21).png>)






## RESULT
The program for implementing image maps using HTML is executed successfully.
