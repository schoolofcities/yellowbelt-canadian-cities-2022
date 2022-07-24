<script>
	import Top from './lib/TopSofC.svelte'
	import CalgaryWeb from './assets/calgary-web.png'
	import TorontoWeb from './assets/toronto-web.png'
	import TorontoPrint from './assets/toronto-print.png'
	import TorontoLegend from './assets/toronto-legend.svg'
</script>

<main>

	<Top/>

	<div class="title">
		<h1><span id="yellow">The Yellowbelt</span></h1>
		<h2>Mapping exclusionary zoning in four Canadian cities</h2>
	</div>

	<div class="text">
		<p>Lorem ipsum blah blah blah</p>
	</div>

	<div class="text">
		<h2>CALGARY</h2>
	</div>


	<div class="map">
		<a href={TorontoPrint}><img src={CalgaryWeb} alt="Calgary Map" /></a>
	</div>

	<div class="text">
		<h2>TORONTO</h2>
	</div>

	<div class="legend">
		<object type="image/svg+xml" data={TorontoLegend}>
		</object>
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
		text-align: center;
		margin-top: 11	0px;
		padding: 0px;
		margin: 0px;
		
	}

	.title {
		margin: auto;
		margin-top: 100px;
		max-width: 800px;
		padding-bottom: 40px;
	}

	h1 {
		font-family: TradeGothicBold, sans-serif;
		color: white;
		font-size: 4rem;
		font-weight: 100;
		line-height: 1.1;
		margin: 2rem auto;
		max-width: 14rem;
	}

	h2 {
		color: white;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
		Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}

	#yellow {
		color: #F1C500;
	}

	.map {
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
	}

	p {
		margin: 1rem auto;
		line-height: 1.35;
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
