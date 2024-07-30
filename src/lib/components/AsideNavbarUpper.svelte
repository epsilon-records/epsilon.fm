<script lang="ts">
	import { page } from '$app/stores';
	import * as Tooltip from '$lib/components/ui/tooltip/index.js';
	import {
		LayoutDashboard,
		Music,
		ClipboardList,
		ShoppingBag,
		Users,
		ChartNoAxesCombined
	} from 'lucide-svelte/icons';

	const navItems = [
		{ href: '/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
		{ href: '/music', icon: Music, label: 'Music' },
		{ href: '/orders', icon: ClipboardList, label: 'Orders' },
		{ href: '/products', icon: ShoppingBag, label: 'Products' },
		{ href: '/customers', icon: Users, label: 'Customers' },
		{ href: '/analytics', icon: ChartNoAxesCombined, label: 'Analytics' }
	];

	$: activeItem = $page.url.pathname.split('/')[1] || 'dashboard';
</script>

<nav class="flex flex-col items-center gap-4 px-2 py-4">
	{#each navItems as { href, icon: Icon, label }}
		<Tooltip.Root>
			<Tooltip.Trigger asChild let:builder>
				<a
					{href}
					class="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8 {activeItem ===
					href.slice(1)
						? 'bg-accent text-accent-foreground'
						: ''}"
					use:builder.action
					{...builder}
				>
					<Icon class="h-5 w-5" />
					<span class="sr-only">{label}</span>
				</a>
			</Tooltip.Trigger>
			<Tooltip.Content side="right">{label}</Tooltip.Content>
		</Tooltip.Root>
	{/each}
</nav>
