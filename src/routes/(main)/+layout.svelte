<script lang="ts">
	import '$src/app.css';
	import Menu from '$lib/components/Menu.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import Aside from '$lib/components/Aside.svelte';
	import Header from '@/components/Header.svelte';
	import { sidebarVisible } from '$lib/stores/ui';
	import PageTransition from '$lib/components/PageTransition.svelte';
	import type { LayoutData } from './$types';

	export let data: LayoutData;
</script>

<SignedIn>
	<div class="flex min-h-screen w-full flex-col bg-muted/40">
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
</SignedIn>
