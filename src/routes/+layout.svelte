<script lang="ts">
	import '../app.css';
	import Header from './Header.svelte';
	import type { LayoutServerData } from './$types';
	import { Badge } from '$lib/components/ui/badge/index.js';

	export let data: LayoutServerData;
</script>

<div class="app">
	<Header></Header>

	<main>
		<slot></slot>
	</main>

	<footer>
		<p>Made with ❤️ by Epsilon</p>
		<Badge>{data.nodeEnv}</Badge>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
