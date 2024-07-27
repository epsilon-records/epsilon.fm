<script lang="ts">
	import '../app.css';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools';
	import type { LayoutData, LayoutServerData } from './$types';
	import { Toaster } from 'svelte-french-toast';

	export let data: LayoutData & LayoutServerData;
</script>

<div class="app flex min-h-screen flex-col">
	<QueryClientProvider client={data.queryClient}>
		<!-- <Header /> -->
		<Toaster />
		<main class="flex flex-grow items-center justify-center">
			<slot></slot>
		</main>
		<footer>
			<p class="m-4 flex flex-grow items-center justify-center text-sm text-muted-foreground">
				Made with ❤️ by Epsilon Records
			</p>
		</footer>
		<SvelteQueryDevtools></SvelteQueryDevtools>
	</QueryClientProvider>
</div>
