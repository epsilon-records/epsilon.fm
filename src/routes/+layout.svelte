<script lang="ts">
	import Loading from '$lib/components/Loading.svelte';
	import StatusBar from '$lib/components/StatusBar.svelte';
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
	import Menu from '$lib/components/Menu.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import Aside from '$lib/components/Aside.svelte';
	import Header from '$lib/components/Header.svelte';
	import { sidebarVisible } from '$lib/stores/ui';
	import MadeWithLove from '$lib/components/MadeWithLove.svelte';
	import { browser } from '$app/environment';

	export let data: LayoutData;
</script>

<div class="app flex min-h-screen flex-col">
	{#if !browser}
		<Loading />
	{:else}
		<ClerkLoading>
			<Loading />
		</ClerkLoading>
		<ClerkLoaded>
			<QueryClientProvider client={data.queryClient}>
				<SignedOut>
					<div class="flex min-h-screen w-full flex-col bg-muted/40">
						<div
							class="flex flex-col sm:gap-4 sm:py-4"
							class:sm:pl-14={$sidebarVisible}
							class:sm:pl-0={!$sidebarVisible}
						>
							<PageTransition key={data.url.pathname}>
								<slot />
							</PageTransition>
							<div class="flex justify-center">
								<MadeWithLove />
							</div>
						</div>
					</div>
				</SignedOut>
				<SignedIn>
					<div class="flex min-h-[calc(100vh-96px)] w-full flex-col bg-muted/40">
						<Menu />
						{#if $sidebarVisible}
							<Aside></Aside>
						{/if}
						<div
							class="flex flex-col sm:gap-4 sm:py-4"
							class:sm:pl-14={$sidebarVisible}
							class:sm:pl-0={!$sidebarVisible}
						>
							<Header />
							<PageTransition key={data.url.pathname}>
								<slot />
							</PageTransition>
						</div>
					</div>
					<Toaster />
					<AudioPlayer />
					<StatusBar />
				</SignedIn>
				<ModeWatcher />
				<SvelteQueryDevtools />
			</QueryClientProvider>
		</ClerkLoaded>
	{/if}
</div>
