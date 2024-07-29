<script lang="ts">
	import Footer from '$lib/components/Footer.svelte';
	import '$src/app.css';
	import { ModeWatcher } from 'mode-watcher';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools';
	import type { LayoutData, LayoutServerData } from './$types';
	import { Toaster } from 'svelte-french-toast';
	import ClerkLoaded from 'clerk-sveltekit/client/ClerkLoaded.svelte';
	import ClerkLoading from 'clerk-sveltekit/client/ClerkLoading.svelte';
	import { Stretch } from 'svelte-loading-spinners';

	export let data: LayoutData & LayoutServerData;
</script>

<div class="app flex min-h-screen flex-col">
	<ClerkLoading>
		<div class="flex h-screen items-center justify-center">
			<Stretch />
		</div>
	</ClerkLoading>
	<ClerkLoaded>
		<QueryClientProvider client={data.queryClient}>
			<slot />
			<Footer></Footer>
			<ModeWatcher />
			<Toaster></Toaster>
			<SvelteQueryDevtools></SvelteQueryDevtools>
		</QueryClientProvider>
	</ClerkLoaded>
</div>
