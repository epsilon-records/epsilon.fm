<script lang="ts">
	import WelcomeCard from '@/components/WelcomeCard.svelte';
	import Dashboard from '$lib/components/Dashboard.svelte';
</script>

<Dashboard>
	<svelte:fragment slot="topLeft">
		<WelcomeCard />
	</svelte:fragment>
	<svelte:fragment slot="topCenter"></svelte:fragment>
	<svelte:fragment slot="topRight"></svelte:fragment>
	<svelte:fragment slot="content"></svelte:fragment>
	<svelte:fragment slot="sidebar"></svelte:fragment>
</Dashboard>
