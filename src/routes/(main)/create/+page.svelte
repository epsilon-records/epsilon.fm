<script lang="ts">
	import Dashboard from '$lib/components/Dashboard.svelte';
</script>

<Dashboard>
	<svelte:fragment slot="topLeft">Create New Release</svelte:fragment>
	<svelte:fragment slot="topCenter"></svelte:fragment>
	<svelte:fragment slot="topRight"></svelte:fragment>
	<svelte:fragment slot="content"></svelte:fragment>
	<svelte:fragment slot="sidebar"></svelte:fragment>
</Dashboard>
