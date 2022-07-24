<script>

	export let city;

	const cities = {
		"calgary": {
			"SD": 0.623,
			"OR": 0.363,
			"MU": 0.014
		}
	}

	const margin = { top: 15, bottom: 25, left: 80, right: 20 };
	let divWidth;
	const height = 150;

	const innerHeight = height - margin.top - margin.bottom;
	$: innerWidth = divWidth - margin.left - margin.right;

	$: boxes = [
		[0, cities[city]["SD"] * divWidth], 
		[cities[city]["SD"] * divWidth, (cities[city]["SD"] + cities[city]["OR"]) * divWidth],
		[(cities[city]["SD"] + cities[city]["OR"]) * divWidth, divWidth]
	]

	$: console.log(boxes)

</script>



<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
	<svg width={divWidth} {height} class="svg-content">

	</svg>
</div>


<style>

	#container {
			padding-left: 0px;
			max-width: 600px;
			background-color: white;
		}

</style>