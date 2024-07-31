<script lang="ts">
	import WelcomeCard from '@/components/WelcomeCard.svelte';
	import StatsCard from '$lib/components/StatsCard.svelte';
	import Dashboard from '$lib/components/Dashboard.svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
</script>

<Dashboard>
	<svelte:fragment slot="topLeft">
		<WelcomeCard />
	</svelte:fragment>
	<svelte:fragment slot="topCenter">
		{#await data}
			<p>Loading stats...</p>
		{:then data}
			<StatsCard trackInfo={data.trackInfo} error={data.error} />
		{:catch error}
			<p>Error loading stats: {error.message}</p>
		{/await}
	</svelte:fragment>
	<svelte:fragment slot="topRight"></svelte:fragment>
	<svelte:fragment slot="content"></svelte:fragment>
	<svelte:fragment slot="sidebar"></svelte:fragment>
</Dashboard>
