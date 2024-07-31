<script lang="ts">
	import WelcomeCard from '$lib/components/WelcomeCard.svelte';
	import StatsCard from '$lib/components/StatsCard.svelte';
	import Dashboard from '$lib/components/Dashboard.svelte';
	import type { PageServerData } from './$types';
	import OrdersThisMonth from '$lib/components/OrdersThisMonth.svelte';
	import OrderTabs from '$lib/components/OrderTabs.svelte';
	export let data: PageServerData;
</script>

<Dashboard>
	<svelte:fragment slot="topLeft">
		<WelcomeCard />
	</svelte:fragment>
	<svelte:fragment slot="topCenter"></svelte:fragment>
	<svelte:fragment slot="topRight">
		<OrdersThisMonth />
	</svelte:fragment>
	<svelte:fragment slot="content"
		>{#await data}
			<p>Loading stats...</p>
		{:then data}
			<StatsCard artistInfo={data.artistInfo} error={data.error} />
			<StatsCard artistInfo={data.artistInfo} error={data.error} />
		{:catch error}
			<p>Error loading stats: {error.message}</p>
		{/await}
	</svelte:fragment>
	<svelte:fragment slot="sidebar">
		<OrderTabs />
	</svelte:fragment>
</Dashboard>
