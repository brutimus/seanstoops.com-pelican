Title: Installing a battery charged by the alternator in a Sprinter camper van conversion
Shorttitle: Electrical
Slug: electrical
Date: 2016-8-5
Category: Van Building
Tags: sprinter, build, build-log
Authors: Sean Stoops
Summary: The electrical side of a van build is something that should be tailored your power requirements. Some people require little more than a few LED lights and obviously don't spend much time worrying about batteries, solar panels and the like. Others want a mega-system that allows them to plug in laptops, kettles, induction stoves, etc.
image: {photo}2016-08-05-electrical-i/electrical.jpg


*Apologies in advance for the total lack of photos for this post. I did my electrical work toward the end of my build when time was running low and I never took a moment to snap a photo. In my upcoming post about the second phase in my electrical work (including solar, fridge, etc.) I will have more photos, I promise!*

#### Materials list

- [WirthCo 125 amp Battery Isolator](http://amzn.to/2aAqeCE)
- [100 amp hour deep cycle battery](http://amzn.to/2aArENt)
- [Fuse block](http://amzn.to/2at3STN)
- [Small fuses](http://amzn.to/2aBzSe7)
- [High amp fuse holder](http://amzn.to/2aVt9Kj)
- [High amp fuses](http://amzn.to/2aAs4DA)

***

The electrical side of a van build is something that should be tailored your power requirements. Some people require little more than a few LED lights and obviously don't spend much time worrying about batteries, solar panels and the like. Others want a mega-system that allows them to plug in laptops, kettles, induction stoves, etc.

For my build, I didn't plan to start out with much -- just a few LED lights, a roof fan and USB plugs for phones and accessories. I did, however, want to leave room for expansion in case I decided to install a 12V fridge at a later date (and as of this writing, I have since installed a 12V fridge and am very glad I over-planned in the beginning).

Allow me to document this in the phases in which I built it.

#### Phase I - Plan

The deadline I had set for myself during the initial build did not allow me enough time to figure out a fridge, or if I even wanted one. So to start with, my electrical needs were relatively minute, but I wanted to build in enough capacity in case I'd return later and redesign things a bit. Over-building in the beginning would be much cheaper and more efficient than trying to retrofit extra capacity later.

The only power requirements I had initially were:

- 3 amps max from the roof fan
- 2 amps max from the LED perimeter lights
- 1 amp from my kitchen lights
- 2 amps or less from the occasional phone charging

Clearly nothing in my build was going to be a power hog. The biggest would be leaving the roof fan on all night when camped in hotter locales; and 1.5 amps (on low) for 8 hours is only 12 amp hours.

So this left me with a few decisions to be made: alternator charging, solar charging, battery size.

Again, with my short deadline and lower power requirements, I didn't see the need in going solar. I figured using a relay between the starting and house batteries would be plenty sufficient. My van came to be equipped with a 200 amp alternator, so I did not need to put any additional thought into the extra load on the vehicle. Given the choice between a simple idiot switch to switch the connection between batteries for around $20 and a voltage sensing relay for around $60, I thought it wise to spend the little bit extra to ensure I never drain my starting battery. I purchased a [WirthCo 125 amp Battery Isolator](http://amzn.to/2aAqeCE).

Now for battery capacity. I hate to tell you, I didn't have any magical formula to determine what battery I needed. The battery would be placed under my passenger seat inside the van with my relay, fuse panel, etc. Just that fact alone meant I'd be looking at non-venting batteries. Lead acid was out. The only two real options left were gel cell and AGM. I'm no battery expert and I certainly didn't become one by doing this research, but in my reading around it seemed gel cells are becoming a thing of the past in most applications and AGM are what's replacing them. So I'd be going with AGM.

The decision between a starting battery and a deep cycle battery is a no-brainer. Starting batteries are meant to deliver short bursts of very high power. This is what you need when turning over a cold engine. Deep cycle batteries deliver a little bit of power but for a very long time. In between these two sits the "marine battery". I still don't fully understand it any further than just knowing that they can deliver high amperage for starting a motor and they will also deliver low amperage for an extended duration. My assumption is, however, that they don't do either job very well. I figured I might as well just find a true deep cycle battery.

Now the question was, how big? It may have just been my desire to have a nice round number, but I chose 100 amp hours. The battery I found would just barely fit into my under-seat box and it would also give me plenty of capacity head room with my current power requirements and even be able to sustain a 12V fridge (assuming roughly 3 amp load and 20% duty cycle) in the future for a couple days without issue. I decided upon [this battery](http://amzn.to/2aArENt).

If you've studied up on your AGM batteries, you'll notice that my charging circuit will not properly charge my AGM battery to full capacity. AGM batteries require a multi-stage charging cycle running through different voltages for varying durations (bulk, float, etc). For long term use, this is not a good way to set it up, but for just a summer, I was okay living with the miniscule damage it may do to my AGM battery until I could come up with a better charging circuit once I returned home from my travels.

The remainder of my electrical components included:

 - [Fuse block](http://amzn.to/2at3STN) & [fuses of varying sizes](http://amzn.to/2aBzSe7) for consumers
 - [High amp fuses](http://amzn.to/2aAs4DA) to protect charging circuit
 - Heavy gauge wire to run between starting and house batteries and between charging components
 - Smaller gauge wire to run to the consumers
 - Ring terminals of varying sizes
 - Heat shrink
 - Misc. connectors, crimper, tape, etc.


#### Phase I - Build

For the sake of clarity, I'll bullet this section out:

1. Run an approximately 12 inch piece of heavy 4 gauge wire from the starting battery to the 100 amp ANL fuse mounted adjacent to the starting battery. It's important to put this fuse as close to the starting battery as possible in case of any electrical shorts down the line. As I mentioned earlier, starting batteries are very good at delivering very high amperage, so any short with such a heavy gauge wire could easily deliver hundreds of amps and cause a fire. **This fuse is critical! Do not install the fuse yet!**
2. Run two much longer pieces of 4 gauge wire, one red and one black, from the starting battery down through the engine bay following the main wiring harness under the vehicle, then up through the weather-proof seat into the *driver seat* box. From here, make a sharp turn and run it through the channel between the driver and passenger seats. The red wire will connect to the other side of the ANL fuse holder and the black wire will connect directly to the negative post on the starting battery. The black (ground) wire is not absolutely necessary as the vehicle chassis doubles as the ground, but I've read you *can* wind up with weird ground loop situations if you ground everything to the chassis. I liked the extra security of just running the ground wire and not worrying about issues.
3. I sat the battery in the under-seat box and measured the remaining space in order to cut out a piece of plywood to fit and give my a surface to mount all my components to. For my battery to fit, it has to be laid on its side.
4. Eyeball the remaining space and arrange the battery isolator/relay and fuse block in a way that leaves sufficient room to connect everything together. Keep in mind a few of these wires will be very heavy gauge and won't bend very tightly.
5. Once happy with the arrangement, screw all the components into place and begin hooking them all together!

I don't have a schematic drawn up just yet, but I'll bullet out how things ought to be wired together. At the end of this post, I've attached the schematic WirthCo provides with the battery isolator which matches my setup almost identically.

Remember: **do not install any fuses until everything is all wired up and you are 100% certain it is correct!**

1. Attach the 4 gauge positive (red) wire coming from the starting battery to the **MAIN +** post of the battery isolator.
2. Run another piece of 4 gauge red wire from the **AUX +** post on the battery isolator to the **+** post on the AGM battery.
3. Connect the 4 gauge black wire coming from the starting battery to the **-** post on the AGM battery.
4. Connect the ground wire of the battery isolator to the **-** post on the AGM battery.
5. Run a small piece of heavier gauge red wire (I used some leftover 4 gauge) from the **+** post on the AGM battery to the post on the fuse block.

At this point, the core system is all hooked together and ready for testing. After checking over every connection several times to ensure everything was tight and no wires were crossed, I went up under the hood and pugged in the 100 amp ANL fuse for just a second then removed it, walked back to make sure nothing was fried or on fire, went back up and plugged it back in for good. The battery isolator lit up and seemed to be operational!

I started the engine to kick the alternator on while monitoring the status lights on the battery isolator. It switched over and began charging my AGM battery! Success!

From here, all of my electrical consumers (fan, lights, etc.) can all be wired back into the fuse block. Again, you only **need** to run the positive wire of the consumer back to the fuse block and the ground wire can simply be attached to the chassis. However, I just like the piece of mind of running the ground back to the negative post of the AGM battery.

When wiring up each consumer, the wire gauge must be selected depending on the current draw of the consumer and the length of the wire run. This part will require a little study on your part as it's easy to miscalculate and end up with a fire hazard.

But as a quick example, let's take my vent fan. On high, it will draw no more than 4 amps. Using a long piece of string, I trace the path the wire will have to take from the fan along the ceiling and down the column beside the passenger seat down to the fuse block. Let's say this is 20 feet. Looking at the following chart, we see that I'm okay to use 16 gauge wire to make this run accepting a non-critical 10% voltage loss.

![Wire chart]({photo}2016-08-05-electrical-i/wire_chart.jpg)

*A note on critical vs non-critical: critical means something like a computer or device that requires exact voltage. Non-critical is referring to simple devices like fans, lights, etc. If you want to prevent any power losses, just use the critical column and oversize your wiring. For a small build like this, this option won't cost you much extra. This becomes a big deal in large projects where there may be miles of wire and a difference of 1 gauge can mean hundreds or thousands of dollars.*

Now cut a piece of 16 gauge wire and run it through this path and connect the ends to the fan and the fuse block. Since we used the 5A column on the chart, it's important that we use no more than a 5A fuse. This way, if the fan malfunctions and begins to draw 20A, the fuse will blow instead of the wire burning up and starting the van on fire. Fuses should always be selected based upon your wire's current capacity.

#### Phase II

This electrical system ended up working great for my first long summer trip and for smaller trips through the rest of the fall and winter. I ended up revisiting my build the following spring to install solar panels, a solar charge controller and a fridge.

I'll be back with a new post about that soon!

---

##### WirthCo Wiring Schematic

![Schematic]({photo}2016-08-05-electrical-i/wirthco_schematic.jpg)
