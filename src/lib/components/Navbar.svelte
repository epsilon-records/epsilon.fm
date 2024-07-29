<script lang="ts">
	import { page } from '$app/stores';
	import LayoutDashboard from 'lucide-svelte/icons/layout-dashboard';
	import ClipboardList from 'lucide-svelte/icons/clipboard-list';
	import ShoppingBag from 'lucide-svelte/icons/shopping-bag';
	import Users from 'lucide-svelte/icons/users';
	import ChartNoAxesCombined from 'lucide-svelte/icons/chart-no-axes-combined';
	import Settings from 'lucide-svelte/icons/settings';
	import * as Tooltip from '$lib/components/ui/tooltip/index.js';

	$: activeItem = $page.url.pathname.startsWith('/dashboard')
		? 'dashboard'
		: $page.url.pathname.startsWith('/orders')
			? 'orders'
			: $page.url.pathname.startsWith('/products')
				? 'products'
				: $page.url.pathname.startsWith('/customers')
					? 'customers'
					: $page.url.pathname.startsWith('/analytics')
						? 'analytics'
						: $page.url.pathname.startsWith('/settings')
							? 'settings'
							: 'dashboard';
</script>

<nav class="flex flex-col items-center gap-4 px-2 py-4">
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="/dashboard"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'dashboard'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<LayoutDashboard class="h-5 w-5" />
				<span class="sr-only">Dashboard</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Dashboard</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="/orders"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'orders'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<ClipboardList class="h-5 w-5" />
				<span class="sr-only">Orders</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Orders</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="/products"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'products'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<ShoppingBag class="h-5 w-5" />
				<span class="sr-only">Products</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Products</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="/customers"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'customers'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<Users class="h-5 w-5" />
				<span class="sr-only">Customers</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Customers</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="/analytics"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'analytics'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<ChartNoAxesCombined class="h-5 w-5" />
				<span class="sr-only">Analytics</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Analytics</Tooltip.Content>
	</Tooltip.Root>
</nav>
<nav class="mt-auto flex flex-col items-center gap-4 px-2 py-4">
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="/settings"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'settings'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<Settings class="h-5 w-5" />
				<span class="sr-only">Settings</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Settings</Tooltip.Content>
	</Tooltip.Root>
</nav>
