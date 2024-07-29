<script lang="ts">
	import House from 'lucide-svelte/icons/house';
	import FileChartLine from 'lucide-svelte/icons/file-chart-line';
	import Package from 'lucide-svelte/icons/package';
	import Package2 from 'lucide-svelte/icons/package-2';
	import PanelLeft from 'lucide-svelte/icons/panel-left';
	import ShoppingCart from 'lucide-svelte/icons/shopping-cart';
	import UsersRound from 'lucide-svelte/icons/users-round';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Sheet from '$lib/components/ui/sheet/index.js';
</script>

<Sheet.Root>
	<Sheet.Trigger asChild let:builder>
		<Button builders={[builder]} size="icon" variant="outline" class="sm:hidden">
			<PanelLeft class="h-5 w-5" />
			<span class="sr-only">Toggle Menu</span>
		</Button>
	</Sheet.Trigger>
	<Sheet.Content side="left" class="sm:max-w-xs">
		<nav class="grid gap-6 text-lg font-medium">
			<a
				href="##"
				class="group flex h-10 w-10 shrink-0 items-center justify-center gap-2 rounded-full bg-primary text-lg font-semibold text-primary-foreground md:text-base"
			>
				<Package2 class="h-5 w-5 transition-all group-hover:scale-110" />
				<span class="sr-only">Epsilon FM</span>
			</a>
			<a
				href="##"
				class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
			>
				<House class="h-5 w-5" />
				Dashboard
			</a>
			<a href="##" class="flex items-center gap-4 px-2.5 text-foreground">
				<ShoppingCart class="h-5 w-5" />
				Orders
			</a>
			<a
				href="##"
				class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
			>
				<Package class="h-5 w-5" />
				Products
			</a>
			<a
				href="##"
				class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
			>
				<UsersRound class="h-5 w-5" />
				Customers
			</a>
			<a
				href="##"
				class="flex items-center gap-4 px-2.5 text-muted-foreground hover:text-foreground"
			>
				<FileChartLine class="h-5 w-5" />
				Settings
			</a>
		</nav>
	</Sheet.Content>
</Sheet.Root>
