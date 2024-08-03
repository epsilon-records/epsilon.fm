<script lang="ts">
	import HomeCard from '@/components/HomeCard.svelte';
	import NewsletterCard from '$lib/components/NewsletterCard.svelte';
	import GitHubCorner from '$lib/components/GitHubCorner.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
</script>

<svelte:head>
	<title>Epsilon FM</title>
	<meta
		name="description"
		content="Our modern open-source music distribution platform includes a beautifully designed artist website, customised merch, generative AI music videos, and access to over one hundred global digital streaming platforms including Beatport, Traxsource, and Juno Download."
	/>
</svelte:head>

<SignedOut>
	<GitHubCorner />
</SignedOut>
<div class="mt-16 flex flex-grow flex-col items-center justify-center">
	<HomeCard></HomeCard>
	<NewsletterCard></NewsletterCard>
</div>
