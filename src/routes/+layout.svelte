<script lang="ts">
	import Loading from '$lib/components/Loading.svelte';
	import StatusBar from '@/components/StatusBar.svelte';
	import '$src/app.css';
	import { ModeWatcher } from 'mode-watcher';
	import { QueryClientProvider } from '@tanstack/svelte-query';
	import { SvelteQueryDevtools } from '@tanstack/svelte-query-devtools';
	import type { LayoutData } from './$types';
	import { Toaster } from 'svelte-french-toast';
	import ClerkLoaded from 'clerk-sveltekit/client/ClerkLoaded.svelte';
	import ClerkLoading from 'clerk-sveltekit/client/ClerkLoading.svelte';
	import PageTransition from '$lib/components/PageTransition.svelte';
	import AudioPlayer from '$lib/components/AudioPlayer.svelte';

	export let data: LayoutData;
</script>

<PageTransition key={data.url.pathname === '/' ? '/' : 'loaded'}>
	<div class="app flex min-h-screen flex-col">
		<ClerkLoading>
			<Loading />
		</ClerkLoading>
		<ClerkLoaded>
			<QueryClientProvider client={data.queryClient}>
				<slot />
				<ModeWatcher />
				<Toaster />
				<AudioPlayer />
				<StatusBar />
				<SvelteQueryDevtools />
			</QueryClientProvider>
		</ClerkLoaded>
	</div>
</PageTransition>
