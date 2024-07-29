<script lang="ts">
	import House from 'lucide-svelte/icons/House';
	import FileChartLine from 'lucide-svelte/icons/file-chart-line';
	import Package from 'lucide-svelte/icons/package';
	import Settings from 'lucide-svelte/icons/settings';
	import ShoppingCart from 'lucide-svelte/icons/shopping-cart';
	import UsersRound from 'lucide-svelte/icons/users-round';
	import * as Tooltip from '$lib/components/ui/tooltip/index.js';

	export let activeItem:
		| 'dashboard'
		| 'orders'
		| 'products'
		| 'customers'
		| 'analytics'
		| 'settings' = 'dashboard';
</script>

<nav class="flex flex-col items-center gap-4 px-2 py-4">
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="##"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'dashboard'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<House class="h-5 w-5" />
				<span class="sr-only">Dashboard</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Dashboard</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="##"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'orders'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<ShoppingCart class="h-5 w-5" />
				<span class="sr-only">Orders</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Orders</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="##"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'products'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<Package class="h-5 w-5" />
				<span class="sr-only">Products</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Products</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="##"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'customers'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<UsersRound class="h-5 w-5" />
				<span class="sr-only">Customers</span>
			</a>
		</Tooltip.Trigger>
		<Tooltip.Content side="right">Customers</Tooltip.Content>
	</Tooltip.Root>
	<Tooltip.Root>
		<Tooltip.Trigger asChild let:builder>
			<a
				href="##"
				class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
				'analytics'
					? 'bg-accent text-accent-foreground'
					: ''}"
				use:builder.action
				{...builder}
			>
				<FileChartLine class="h-5 w-5" />
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
