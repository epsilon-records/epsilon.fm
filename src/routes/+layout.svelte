<script lang="ts">
	import '../app.css';
	import Header from './Header.svelte';
	import type { LayoutServerData } from './$types';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { ModeWatcher } from 'mode-watcher';
	import { Separator } from '$lib/components/ui/separator';
	import { Toaster } from 'svelte-french-toast';
	import PageTransition from '$lib/components/PageTransition.svelte';
	import ClerkLoaded from 'clerk-sveltekit/client/ClerkLoaded.svelte';
	import ClerkLoading from 'clerk-sveltekit/client/ClerkLoading.svelte';
	export let data: LayoutServerData;
</script>

<div class="app">
	<Header></Header>

	<main>
		<ModeWatcher />
		<PageTransition pathname={data.pathname}>
			<ClerkLoading>
				<div class="m-4">Loading...</div>
			</ClerkLoading>
			<ClerkLoaded let:clerk>
				<slot {clerk} />
			</ClerkLoaded>
		</PageTransition>
		<Toaster />
	</main>

	<footer>
		<p class="text-sm text-muted-foreground">Made with ❤️ by Epsilon Records</p>
		<Badge class="m-2" variant={data.nodeEnv == 'development' ? 'outline' : 'default'}
			>{data.nodeEnv}</Badge
		>
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
