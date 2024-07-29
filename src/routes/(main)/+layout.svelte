<script lang="ts">
	import '$src/app.css';
	import Menu from '$lib/components/Menu.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import Aside from '$lib/components/Aside.svelte';
	import Header from '$lib/components/Header.svelte';
</script>

<SignedIn>
	<div class="flex min-h-screen w-full flex-col bg-muted/40">
		<Menu />
		<Aside></Aside>
		<div class="flex flex-col sm:gap-4 sm:py-4 sm:pl-14">
			<Header></Header>
			<slot />
		</div>
	</div>
</SignedIn>
