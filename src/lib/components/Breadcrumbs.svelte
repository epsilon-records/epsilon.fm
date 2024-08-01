<script lang="ts">
	import * as Breadcrumb from '$lib/components/ui/breadcrumb/index.js';
	import { page } from '$app/stores';

	$: routes = $page.url.pathname.split('/').filter(Boolean);
	$: breadcrumbs = routes.map((route, index) => ({
		name: route.charAt(0).toUpperCase() + route.slice(1),
		href: '/' + routes.slice(0, index + 1).join('/')
	}));
</script>

<Breadcrumb.Root class="hidden md:flex">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		{#each breadcrumbs as crumb, index}
			<Breadcrumb.Separator />
			<Breadcrumb.Item>
				{#if index === breadcrumbs.length - 1}
					<Breadcrumb.Page>{crumb.name}</Breadcrumb.Page>
				{:else}
					<Breadcrumb.Link href={crumb.href}>{crumb.name}</Breadcrumb.Link>
				{/if}
			</Breadcrumb.Item>
		{/each}
	</Breadcrumb.List>
</Breadcrumb.Root>
