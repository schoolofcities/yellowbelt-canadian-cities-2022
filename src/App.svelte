<script>
	import Top from "./lib/TopSofC.svelte";
	import CalgaryWeb from "./assets/calgary-web.png";
	import EdmontonWeb from "./assets/edmonton-web.png";
	import TorontoWeb from "./assets/toronto-web.png";
	import VancouverWeb from "./assets/vancouver-web.png";
	import LegendBar from "./lib/LegendBar.svelte";
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
</svelte:head>

<main>

	<Top />

	<div class="title">
		<h1>Mapping exclusionary residential zoning in four Canadian cities</h1>
		<p><a href="https://jamaps.github.io">Jeff Allen</a> | July 2022</p>
	</div>

	<div class="text">
		<p>
			We've created maps of Canadian cities showing how <span id="yellow"><b>more than 50%</b></span> of the land zoned for residential development in most cities <span id="yellow"><b>only allows for single detached homes</b></span>.
		</p>
		<p>
			<a href="https://en.wikipedia.org/wiki/Exclusionary_zoning">Exclusionary zoning</a> for only single detached housing (i.e. the <a href="http://www.mapto.ca/maps/2017/3/4/the-yellow-belt">Yellowbelt</a>) strictly limits the diversity and density of housing that can be built in a neighbourhood. Lack of supply of housing within cities, particularly the <a href="https://99percentinvisible.org/episode/the-missing-middle/">missing middle</a>, has been cited as a key driver for <a href="https://trreb.ca/hlfiles/pdf/2021.01.04-TRREB_Missing_Middle.pdf">rising housing prices</a> (among <a href="https://www.youtube.com/watch?v=wP3uQUZlhdo&t=0s">other factors</a>). Because of their low density, single detached neighbourhoods are also less walkable (i.e. are more <a href = "https://www150.statcan.gc.ca/n1/en/pub/11-008-x/2008001/article/10503-eng.pdf?st=qvzoFyxE">car dependent</a>), which has wider negative environmental and population health effects. As such, there have been several <a href="https://chbooks.com/Books/H/House-Divided">calls</a> to <a href="https://www.tvo.org/article/end-exclusionary-zoning-says-torontos-board-of-trade">end</a> exclusionary zoning in Canadian cities.
		</p>
		<p>
			Below we categorize and map zoning by-laws for four Canadian cities. Each city has dozens of unique zoning categorizations, so to create comparative maps, we've gone through each city's zoning by-law and aggregated into three distinct classifications:
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
			<span class="zone-icon-info">Can only build single detached homes on properties. In some zones, owners can build detached secondary suites</span>
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
			<span class="zone-icon-info">Can build single detached, semi-detached, townhouses, -plexes, and/or apartments - but no mixed use buildings</span>
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
			<span class="zone-icon-info">Same as above, but can also develop buildings that have residences mixed with other uses such as retail and offices</span>
		</p>
		<p>
			This page and its content (maps, code for cleaning and categorizing data, etc.) are hosted on <a href="https://github.com/schoolofcities/yellowbelt-canadian-cities-2022">GitHub</a>
		</p>
	</div>

	
	
	<div class="text">
		<h2>CALGARY</h2>
		<LegendBar city="calgary" />
	</div>

	<div class="map">
		<img src={CalgaryWeb} alt="Calgary Map" />
	</div>

	<div class="info">
		<p>
			<b>| More Information | </b>
			<br>
			<span id="info-links"><a href="https://www.calgary.ca/planning/land-use/online-land-use-bylaw.html">Zoning By-Law</a> | <a href="https://data.calgary.ca/Base-Maps/Land-Use-Districts/mw9j-jik5">Spatial Data</a> | <a href="https://raw.githubusercontent.com/schoolofcities/yellowbelt-canadian-cities-2022/main/data/calgary/calgary-print.png">High Resolution Map</a></span>
			<b>| Zoning Categories |</b>
		</p>
	</div>

	<div class="categories">
		<code>
			<b>Single Detached Zones:</b><br> R-1, R-1N, R-1s, R-C1, R-C1L, R-C1Ls, R-C1N, R-C1s, R-MH <br>
			<b>Other Residential Zones:</b><br> CC-MH, M-1, M-2, M-C1, M-C2, M-CG, M-G, M-H1, M-H2, M-H3, M-X1, M-X2, R-2, R-2M, R-C2, R-CG, R-CG-ex, R-G, R-Gm <br>
			<b>Mixed Use Zones:</b><br> CC-EIR, CC-EMU, CC-EPR, CC-ER, CC-ERR, CC-ET, CC-MHX, CC-X, CR20-C20/R20, MU-1, MU-2
		</code>
	</div>



	<div class="text">
		<h2>EDMONTON</h2>
		<LegendBar city="edmonton" />
	</div>

	<div class="map">
		<img src={EdmontonWeb} alt="Edmonton Map" />
	</div>

	<div class="info">
		<p>
			<b>| More Information | </b>
			<br>
			<span id="info-links"><a href="https://webdocs.edmonton.ca/InfraPlan/zoningbylaw/bylaw_12800.htm">Zoning By-Law</a> | <a href="https://data.edmonton.ca/Thematic-Features/Zoning-Bylaw-Geographical-Data/fixa-tstc">Spatial Data</a> | <a href="https://raw.githubusercontent.com/schoolofcities/yellowbelt-canadian-cities-2022/main/data/edmonton/edmonton-print.png">High Resolution Map</a></span>
			<b>| Zoning Categories |</b>
		</p>
	</div>

	<div class="categories">
		<code>
			<b>Single Detached Zones:</b><br> CCSF, RMH, RPL, RR, RSL, TSDR, TSLR <br>
			<b>Other Residential Zones:</b><br> CCLD, GHLD, GLD, GLG, RF1, RF2, RF3, RF4, RLD, RMD <br>
			<b>Mixed Use Zones:</b><br> AED, BLMR, BRH, CB3, CCA, CCHD, CCMD, CMU, GVC, HA, HDR, HVRH, JAMSC, MMS, MMUT, RA7, RA7a, RA7g, RA8, RA8g, RA8h, RA9, RF5, RF5g, RF5T, R6, RMU, RTCMR, RVRH, SLD, SRA, SRH, TMU, UCRH, UVCa, UW
		</code>
	</div>



	<div class="text">
		<h2>TORONTO</h2>
		<LegendBar city="toronto" />
	</div>

	<div class="map">
		<img src={TorontoWeb} alt="Toronto Map" />
	</div>

	<div class="info">
		<p>
			<b>| More Information | </b>
			<br>
			<span id="info-links"><a href="https://www.toronto.ca/zoning/bylaw_amendments/ZBL_NewProvision_Chapter1.htm">Zoning By-Law</a> | <a href="https://open.toronto.ca/dataset/zoning-by-law/">Spatial Data</a> | <a href="https://raw.githubusercontent.com/schoolofcities/yellowbelt-canadian-cities-2022/main/data/toronto/toronto-print.png">High Resolution Map</a></span>
			<b>| Zoning Categories |</b>
		</p>
	</div>

	<div class="categories">
		<code>
			<b>Single Detached Zones:</b><br> RD <br>
			<b>Other Residential Zones:</b><br> R, RA, RM, RS, RS <br>
			<b>Mixed Use Zones:</b><br> RAC, CR, CRE
		</code>
	</div>



	<div class="text">
		<h2>VANCOUVER</h2>
		<LegendBar city="vancouver" />
	</div>

	<div class="map">
		<img src={VancouverWeb} alt="Vancouver Map" />
	</div>

	<div class="info">
		<p>
			<b>| More Information | </b>
			<br>
			<span id="info-links"><a href="https://vancouver.ca/home-property-development/zoning-and-land-use-policies-document-library.aspx">Zoning By-Law</a> | <a href="https://opendata.vancouver.ca/explore/dataset/zoning-districts-and-labels/information/?disjunctive.zoning_classification&disjunctive.zoning_category&disjunctive.zoning_district">Spatial Data</a> | <a href="https://raw.githubusercontent.com/schoolofcities/yellowbelt-canadian-cities-2022/main/data/vancouver/vancouver-print.png">High Resolution Map</a></span>
			<b>| Zoning Categories |</b>
		</p>
	</div>

	<div class="categories">
		<code>
			<b>Single Detached Zones:</b><br> RA, RS, FSHCA <br>
			<b>Other Residential Zones:</b><br> RT, RM, FM <br>
			<b>Mixed Use Zones:</b><br> HA, FC, C, DD, DEOD, FCCDD
		</code>
		<p>
			For Vancouver, the single detached only zones also allow duplexes. There were also hundreds of CD-1 (Comprehensive Development) zones, each with their own specific allowances. These were categorized based on joining to Metro Vancouver's 2016 land use <a href="http://www.metrovancouver.org/data">data</a>. 
		</p>
	</div>

</main>



<style>
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: 'Roboto', sans-serif;
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
	.title p {
		color: #1e3765;
	}

	.title a {
		color: #1e3765;
	}

	h1 {
		font-family: TradeGothicBold, sans-serif;
		color: #1e3765;
		font-size: 42px;
		font-weight: 100;
		line-height: 1.1;
		max-width: 600px;
	}

	h2 {
		color: white;
		font-family: 'Roboto', sans-serif;
	}

	p {
		color: white;
		margin: 1rem auto;
		line-height: 1.55;
		font-size: 17px;
		font-family: 'Roboto', sans-serif;
	}

	a {
		text-decoration: underline;
		color: #f1c500;
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
		padding-bottom: 5px;
		position: relative;
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

	.info {
		margin: auto;
		color: white;
		max-width: 600px;
		width: calc(100% - 50px);
		padding: 25px;
		padding-top: 0px;
		padding-bottom: 0px;
	}
	.info p {
		font-size: 15px;
		line-height: 2;
	}
	#info-links {
		margin-left: 8px;
		display: block;
	}

	.categories {
		margin: auto;
		color: white;
		max-width: 600px;
		width: calc(100% - 50px);
		padding: 25px;
		padding-top: 0px;
		padding-bottom: 50px;
		margin-top: -10px;
		
	}
	.categories p {
		font-size: 12px;
		margin-left: 8px;
	}
	code {
		font-size: 11px;
		margin-left: 8px;
		display: block;
		line-height: 1.5;
	}

	@media (min-width: 480px) {
		h1 {
			max-width: none;
		}

		p {
			max-width: none;
		}
	}

	@media (max-width: 480px) {
		.categories p {
			font-size: 11px;
		}
		code {
			font-size: 10px;
		}
	}
</style>
