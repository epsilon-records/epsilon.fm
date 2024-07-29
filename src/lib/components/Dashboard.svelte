<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Aside from '$lib/components/Aside.svelte';
	import CreateNewRelease from '$lib/components/CreateNewRelease.svelte';
	import OrdersThisWeek from '$lib/components/OrdersThisWeek.svelte';
	import OrdersThisMonth from '$lib/components/OrdersThisMonth.svelte';
	import OrderTabs from '$lib/components/OrderTabs.svelte';
	import OrderDetails from '$lib/components/OrderDetails.svelte';
	import Menu from '$lib/components/Menu.svelte';
</script>

<div class="flex min-h-screen w-full flex-col bg-muted/40">
	<Menu />
	<Aside></Aside>
	<div class="flex flex-col sm:gap-4 sm:py-4 sm:pl-14">
		<Header></Header>
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
	</div>
</div>
