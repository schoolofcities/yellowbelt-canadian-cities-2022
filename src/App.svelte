<script>
	import Top from "./lib/TopSofC.svelte";
	import CalgaryWeb from "./assets/calgary-web.png";
	import CalgaryPrint from "./assets/calgary-print.png";
	import TorontoWeb from "./assets/toronto-web.png";
	import TorontoPrint from "./assets/toronto-print.png";
	import LegendBar from "./lib/LegendBar.svelte";
</script>

<main>
	<Top />

	<div class="title">
		<h1>Mapping exclusionary residential zoning in four Canadian cities</h1>
		<p><a href="https://jamaps.github.io">Jeff Allen</a> | July 2022</p>
	</div>

	<div class="text">
		<p>
			We've created maps of Canadian cities showing
			how <span id="yellow"><b>more than 50%</b></span> of the land zoned for
			residential development <span id="yellow"><b>only allows for single detached homes</b></span>.
		</p>

		<p>
			<a href="https://en.wikipedia.org/wiki/Exclusionary_zoning"
				>Exclusionary zoning</a
			> for only single detached housing (i.e. the <a href="http://www.mapto.ca/maps/2017/3/4/the-yellow-belt">Yellowbelt</a>) strictly limits the diversity and density of housing that can be
			built in a neighbourhood. Lack of supply of housing within
			cities, particularly the <a href="https://99percentinvisible.org/episode/the-missing-middle/">missing middle</a>, has been cited as a key driver
			for <a href="https://trreb.ca/hlfiles/pdf/2021.01.04-TRREB_Missing_Middle.pdf">rising housing prices</a> (among <a href="https://www.youtube.com/watch?v=wP3uQUZlhdo&t=0s">other factors</a>). Because of their low density, single detached neighbourhoods are
			also less walkable (i.e. are more car dependent), which has wider
			negative environmental and population health effects. As such, there
			have been several calls to <a href="https://www.tvo.org/article/end-exclusionary-zoning-says-torontos-board-of-trade">end</a> exclusionary zoning in Canadian cities.
		</p>

		<p>
			Below we categorize and map zoning by-laws for four Canadian cities.
			Each city has dozens of unique zoning categorizations, so to create
			comparitive maps, we've gone through each city's zoning by-law and
			aggregated into three distinct classifications:
		</p>

		<p>
			<svg class="zone-icons">
				<rect
					x="0"
					y="0"
					width="20"
					height="20"
					style="fill:#F1C500;stroke:white;stroke-width:1;"
				/>
				<text class="zone-icon-label" x="30" y="16" fill="white"
					>Single Detached Only</text
				>
			</svg>
			<br />
			<span class="zone-icon-info"
				>Can only build single detached homes on properties. In some
				zones, owners can build detached secondary suites</span
			>
		</p>

		<p>
			<svg class="zone-icons">
				<rect
					x="0"
					y="0"
					width="20"
					height="20"
					style="fill:#00A189;stroke:white;stroke-width:1;"
				/>
				<text class="zone-icon-label" x="30" y="16" fill="white"
					>Other Residential</text
				>
			</svg>
			<br />
			<span class="zone-icon-info"
				>Can build single detached, semi-detached, townhouses, -plexes,
				and/or apartments - but no mixed use builidings</span
			>
		</p>

		<p>
			<svg class="zone-icons">
				<rect
					x="0"
					y="0"
					width="20"
					height="20"
					style="fill:#6FC7EA;stroke:white;stroke-width:1;"
				/>
				<text class="zone-icon-label" x="30" y="16" fill="white"
					>Mixed Use</text
				>
			</svg>
			<br />
			<span class="zone-icon-info"
				>Same as above, but can also develop buildings that have
				residences mixed with other uses such as retail and offices</span
			>
		</p>
		<br />
	</div>

	<div class="text">
		<h2>CALGARY</h2>
		<a href={CalgaryPrint}>Click here for higher resolution</a>
		<LegendBar city="calgary" />
	</div>

	<div class="map">
		<img src={CalgaryWeb} alt="Calgary Map" />
	</div>
	

	<div class="text">
		<h2>TORONTO</h2>
		<LegendBar city="toronto" />
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
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: #1e3765;
	}

	main {
		margin-top: 11 0px;
		padding: 0px;
		margin: 0px;
	}

	.title {
		text-align: center;
		margin: auto;
		margin-top: 100px;
		margin-bottom: 50px;
		border-top: solid 1px white;
		border-bottom: solid 1px white;
		padding: 15px;
		padding-bottom: 20px;
		background-color: #f1c500;
	}

	h1 {
		font-family: TradeGothicBold, sans-serif;
		color: #1e3765;
		font-size: 42px;
		font-weight: 100;
		line-height: 1.1;
		max-width: 600px;
	}

	.title p {
		color: #1e3765;
	}

	.title a {
		color: #1e3765;
	}

	h2 {
		color: white;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}

	p {
		color: white;
		margin: 1rem auto;
		line-height: 1.55;
		font-size: 17px;
		font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
			Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
	}

	a {
		text-decoration: underline;
		color: #f1c500;
		/* font-weight: bold; */
	}

	#yellow {
		color: #f1c500;
	}

	.zone-icons {
		width: 225px;
		height: 20px;
	}
	.zone-icon-label {
		font-size: 18px;
		font-weight: bold;
	}
	.zone-icon-info {
		font-size: 15px;
		margin-left: 30px;
		display: block;
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

	.text {
		border-top: dashed 1px white;
		margin: auto;
		color: white;
		max-width: 600px;
		width: calc(100% - 50px);
		padding: 25px;
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
