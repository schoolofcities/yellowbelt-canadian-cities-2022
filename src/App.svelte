<script>
	import Top from './lib/TopSofC.svelte'
</script>

<main>
	<Top/>
	<div class="title">
		<h1>Hello world!</h1>
	</div>
	
	<p>
		(Simple <a href="https://svelte.dev">Svelte</a> page to build upon from)
	</p>
</main>

<style>
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
		margin-top: 100px;
		padding: 0px;
		margin: 0px;
		
	}

	.title {
		margin-top: 100px;
	}

	h1 {
		color: white;
		text-transform: uppercase;
		font-size: 4rem;
		font-weight: 100;
		line-height: 1.1;
		margin: 2rem auto;
		max-width: 14rem;
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
