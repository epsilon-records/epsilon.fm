<script lang="ts">
	import '../../app.css';
	import type { LayoutServerData, PageData } from './$types';
	import { Badge } from '$lib/components/ui/badge/index.js';
	export let data: LayoutServerData & PageData;
</script>

<div class="app">
	<main>
		<slot />
	</main>
	<footer>
		<p class="text-muted-foreground text-sm">Made with ❤️ by Epsilon Records</p>
		<Badge class="m-2" variant={data.env === 'development' ? 'outline' : 'default'}>
			{data.env}: {data.gitCommitSha ?? 'unknown'}
		</Badge>
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
		margin: 0 auto;
		box-sizing: border-box;
		max-width: 64rem;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}

	@media (min-width: 900px) {
		:global(body) {
			padding: 0 100px;
		}
	}

	:global(body) {
		font-family: 'Fira Code', monospace;
	}

	@font-face {
		font-family: 'Fira Code', monospace;
		font-display: optional;
		src: url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap');
	}
</style>
