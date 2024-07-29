<script lang="ts">
	import CreateNewRelease from '$lib/components/CreateNewRelease.svelte';
	import OrdersThisWeek from '$lib/components/OrdersThisWeek.svelte';
	import OrdersThisMonth from '$lib/components/OrdersThisMonth.svelte';
	import OrderTabs from '$lib/components/OrderTabs.svelte';
	import OrderDetails from '$lib/components/OrderDetails.svelte';
</script>

<main
	class="grid flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8 lg:grid-cols-3 xl:grid-cols-3"
>
	<div class="grid auto-rows-max items-start gap-4 md:gap-8 lg:col-span-2">
		<div class="grid gap-4 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4">
			<CreateNewRelease></CreateNewRelease>
			<OrdersThisWeek></OrdersThisWeek>
			<OrdersThisMonth></OrdersThisMonth>
		</div>
		<OrderTabs></OrderTabs>
	</div>
	<div>
		<OrderDetails></OrderDetails>
	</div>
</main>
