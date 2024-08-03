<script lang="ts">
	import WelcomeCard from '$lib/components/WelcomeCard.svelte';
	import StatsCard from '$lib/components/StatsCard.svelte';
	import Dashboard from '$lib/components/Dashboard.svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
</script>

<Dashboard>
	<svelte:fragment slot="topLeft">
		<WelcomeCard />
	</svelte:fragment>
	<svelte:fragment slot="topCenter"></svelte:fragment>
	<svelte:fragment slot="topRight"></svelte:fragment>
	<svelte:fragment slot="content">
		{#await data then { artistInfo, error }}
			<StatsCard {artistInfo} {error} />
		{/await}
	</svelte:fragment>
	<svelte:fragment slot="sidebar"></svelte:fragment>
</Dashboard>
