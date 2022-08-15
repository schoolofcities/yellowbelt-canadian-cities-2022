<script>

	export let city;

	const cities = {
		"calgary": {
			"SD": 62.3,
			"OR": 36.3,
			"MU": 1.4
		},
		"toronto": {
			"SD": 54.3,
			"OR": 39.9,
			"MU": 5.8
		},
		"edmonton": {
			"SD": 20.7,
			"OR": 64.0,
			"MU": 15.3
		},
		"vancouver": {
			"SD": 63.8,
			"OR": 24.9,
			"MU": 11.3
		}
	}

	const margin = { top: 1, bottom: 1, left: 1, right: 1 };
	let divWidth;
	const height = 90;

	$: innerWidth = divWidth - margin.left - margin.right;

	$: boxes = [
		[0, cities[city]["SD"] / 100 * innerWidth], 
		[cities[city]["SD"] / 100 * innerWidth, cities[city]["OR"] / 100 * innerWidth],
		[(cities[city]["SD"] / 100 + cities[city]["OR"] / 100) * innerWidth, cities[city]["MU"] / 100 * innerWidth]
	]

	$: label_pts = boxes.map(b =>
		Math.min(b[0], divWidth - 34)
	)

	function toPercent(x) {
		return(parseFloat(x).toFixed(1)+"%")
	}

</script>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
	<svg width={divWidth} {height} class="svg-content">
		<g transform={`translate(${margin.left},${margin.top})`}>
			<text x={label_pts[0]} y="15" fill="white">{toPercent(cities[city]["SD"])}</text>
			<text x={label_pts[1]} y="15" fill="white">{toPercent(cities[city]["OR"])}</text>
			<text x={label_pts[2]} y="15" fill="white">{toPercent(cities[city]["MU"])}</text>

			<text x={boxes[0][0]} y="60" fill="white">Single Detached Only</text>
			<text x={Math.min(divWidth - 132,Math.max(boxes[1][0],165))} y="60" fill="white">Other Residential</text>
			<text x={divWidth - 1} y="80" text-anchor="end" fill="white">Mixed Use</text>

			<line x1={divWidth - 5} y1="45" x2={divWidth - 5} y2="65" style="stroke:white;stroke-width:2" />

			<rect x={boxes[0][0]} y="20" width={boxes[0][1]} height="20"
			style="fill:#F1C500;stroke:white;stroke-width:1;" />
			<rect x={boxes[1][0]} y="20" width={boxes[1][1]} height="20"
			style="fill:#00A189;stroke:white;stroke-width:1;" />
			<rect x={boxes[2][0]} y="20" width={boxes[2][1]} height="20"
			style="fill:#6FC7EA;stroke:white;stroke-width:1;" />
		</g>
	</svg>
</div>


<style>

	#container {
			padding-left: 0px;
			max-width: 600px;
		}

</style>
