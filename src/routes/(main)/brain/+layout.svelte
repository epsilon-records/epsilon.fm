<script lang="ts">
	import { browser } from '$app/environment';
	import Header from '@/components/Header.svelte';

	import { resolvedTheme } from '$lib/theme';
	import '@fontsource/inter';
	import '@fontsource/jetbrains-mono';
	import '$src/app.css';
	import type { LayoutServerData } from './$types';
	import { onDestroy } from 'svelte';

	export let data: LayoutServerData;
	const { chats } = data;

	onDestroy(
		resolvedTheme.subscribe((value) => {
			if (!browser) return;
			document.documentElement.classList.remove('light', 'dark');
			document.documentElement.classList.add(value);
		})
	);
</script>

<svelte:head>
	<title>SvelteKit AI Chatbot</title>
</svelte:head>

{#await chats}
	<p>Loading chats...</p>
{:then chats}
	<Header {chats} />
{:catch error}
	<p>Error loading chats: {error.message}</p>
{/await}
<main class="flex flex-1 flex-col bg-muted/50">
	<slot />
</main>
