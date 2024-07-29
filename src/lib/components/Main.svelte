<script lang="ts">
	import '$src/app.css';
	import WelcomeCard from '$lib/components/WelcomeCard.svelte';
	import NewsletterCard from '$lib/components/NewsletterCard.svelte';
	import GitHubCorner from '$lib/components/GitHubCorner.svelte';
	import Menu from '$lib/components/Menu.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import Aside from '$lib/components/Aside.svelte';
</script>

<SignedIn>
	<div class="flex min-h-screen w-full flex-col bg-muted/40">
		<Menu />
		<div class="flex flex-grow">
			<Aside></Aside>
			<div class="ml-14 flex-grow p-4">
				<slot />
			</div>
		</div>
	</div>
</SignedIn>
<SignedOut>
	<div class="flex flex-grow items-center justify-center">
		<GitHubCorner />
		<WelcomeCard></WelcomeCard>
		<NewsletterCard></NewsletterCard>
	</div>
</SignedOut>
