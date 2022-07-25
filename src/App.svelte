<script>
	import Top from './lib/TopSofC.svelte'
	import CalgaryWeb from './assets/calgary-web.png'
	import CalgaryPrint from './assets/calgary-print.png'
	import TorontoWeb from './assets/toronto-web.png'
	import TorontoPrint from './assets/toronto-print.png'
	import LegendBar from './lib/LegendBar.svelte'
</script>

<main>

	<Top/>

	<div class="title">
		<h1><span id="yellow">The Yellowbelt</span></h1>
		<h2>Mapping exclusionary residential zoning in four Canadian cities</h2>
		<p>-</p>
		<p><a href="https://jamaps.github.io">Jeff Allen</a> | July 2022</p>
	</div>

	<div class="text">
		<p>
			
		While the housing crises is certainly complex and has many causes, one important part being a lack of supply of housing. Zoning for only single detached housing strictly limits the diversity and density of housing that can be built in a neighbourhood.

		These also contribute to neighbourhoods that are not very walkable, QQQQ, and 
		
		Below we map such exclusionary residential zoning in four Canadian cities, showing how in all, more than 50% of the land zoned for residential development only allows for single detached homes 
	
		</p>


		<p>Each city has dozens (and often different) zoning categorizations. To allow for comparison, we've aggregated these into three distinct types:</p>

		<p>
			<svg class="zone-icons">
				<rect x="0" y="0" width="20" height="20"
				style="fill:#F1C500;stroke:white;stroke-width:1;" />
			</svg> 
			<b>Single Detached Only</b><br>(Can only build single detached homes on properties. In some zones, owners can build detached secondary suites)
		</p>
		
		<p>
			<svg class="zone-icons">
				<rect x="0" y="0" width="20" height="20"
				style="fill:#00A189;stroke:white;stroke-width:1;" />
			</svg> 
			<b>Other Residential</b><br>(single detached, semi-detached, townhouses, -plexes, and/or apartments - but no mixed use builidings)
		</p>
		
		<p>
			<svg class="zone-icons">
				<rect x="0" y="0" width="20" height="20"
				style="fill:#6FC7EA;stroke:white;stroke-width:1;" />
			</svg> 
			<b>Mixed Use</b><br>(can develop buildings that have residences mixed with other uses such as retail and offices)
		</p>

			

		<p></p>
		<br>
		<br>
	</div>

	<div class="text">
		<h2>CALGARY</h2>
		<LegendBar city="calgary"/>
	</div>

	


	<div class="map">
		<a href={CalgaryPrint}><img src={CalgaryWeb} alt="Calgary Map" /></a>
	</div>

	<div class="text">
		<h2>TORONTO</h2>
		<LegendBar city="toronto"/>
	</div>

	<div class="map">
		<a href={TorontoPrint}><img src={TorontoWeb} alt="Toronto Map" /></a>
	</div>
	
</main>

<style>
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: #1E3765;
	}

	main {
		margin-top: 11	0px;
		padding: 0px;
		margin: 0px;
		
	}

	.title {
		text-align: center;
		margin: auto;
		margin-top: 50px;
		max-width: 800px;
		padding: 15px;
		padding-bottom: 40px;
	}

	h1 {
		font-family: TradeGothicBold, sans-serif;
		color: white;
		font-size: 4rem;
		font-weight: 100;
		line-height: 1.1;
		
	}

	h2 {
		color: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}

	p {
		color: white;	
		margin: 1rem auto;
		line-height: 1.55;
		font-size: 17px;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}

	a {
		text-decoration: none;
		color: #6FC7EA;
		font-weight: bold;
	}

	#yellow {
		color: #F1C500;
	}

	.zone-icons {
			width: 200px;
			height: 20px;
		}

	.map {
		text-align: center;
		padding-bottom: 45px;
		position: relative;
	}

	.map img:hover {
		border-right: dashed 1px white;
		border-left: dashed 1px white;
		opacity: 0.97;
	}

	.map img {
		max-width: 1200px;
		min-width: 350px;
		width: 100%;
	}

	.legend	 {
		z-index: 1;
		margin: auto;
		text-align: center;
		max-width: 450px;
		min-width: 350px;
		width: 100%;
	}

	.text {
		border-top: dashed 1px white;
		margin: auto;
		color: white;
		max-width: 600px;
		width: 100%;
		padding: 15px;
	}

	

	@media (min-width: 480px) {
		h1 {
			max-width: none;
		}

		p {
			max-width: none;
		}
	}
</style>
