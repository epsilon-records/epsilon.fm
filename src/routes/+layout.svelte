<script lang="ts">
	import '../app.css';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools';
	import type { LayoutData, LayoutServerData } from './$types';
	import { Toaster } from 'svelte-french-toast';

	export let data: LayoutData & LayoutServerData;
</script>

<svelte:head>
	<script async={false} defer src="https://buttons.github.io/buttons.js"></script>
</svelte:head>

<div class="app flex min-h-screen flex-col">
	<QueryClientProvider client={data.queryClient}>
		<Toaster></Toaster>
		<main class="flex flex-grow items-center justify-center">
			<slot></slot>
		</main>
		<footer>
			<p class="flex flex-grow items-center justify-center text-sm">
				Made with ❤️ by&nbsp;<a href="https://epsilonrecords.nl">Epsilon Records</a>
			</p>
			<p class="flex flex-grow items-center justify-center pb-4 pt-2 text-sm">
				<a
					class="github-button"
					href="https://github.com/epsilon-records/epsilon.fm"
					data-color-scheme="no-preference: light; light: light; dark: dark;"
					data-icon="octicon-star"
					data-show-count="true"
					aria-label="Star epsilon-records/epsilon.fm on GitHub">Star</a
				>
			</p>
		</footer>
		<SvelteQueryDevtools></SvelteQueryDevtools>
	</QueryClientProvider>
</div>
