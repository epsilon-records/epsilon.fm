<script lang="ts">
	import WelcomeCard from '@/components/WelcomeCard.svelte';
	import Dashboard from '$lib/components/Dashboard.svelte';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
</script>

<Dashboard>
	<svelte:fragment slot="topLeft">
		<SignedIn let:user>
			<WelcomeCard firstName={user?.firstName ?? ''}></WelcomeCard>
		</SignedIn>
	</svelte:fragment>
	<svelte:fragment slot="topCenter">
		<SignedIn let:user>
			<WelcomeCard firstName={user?.firstName ?? ''}></WelcomeCard>
		</SignedIn>
	</svelte:fragment>
	<svelte:fragment slot="topRight">
		<SignedIn let:user>
			<WelcomeCard firstName={user?.firstName ?? ''}></WelcomeCard>
		</SignedIn>
	</svelte:fragment>
	<svelte:fragment slot="content">
		<SignedIn let:user>
			<WelcomeCard firstName={user?.firstName ?? ''}></WelcomeCard>
		</SignedIn>
	</svelte:fragment>
	<svelte:fragment slot="sidebar">
		<SignedIn let:user>
			<WelcomeCard firstName={user?.firstName ?? ''}></WelcomeCard>
		</SignedIn>
	</svelte:fragment>
</Dashboard>
