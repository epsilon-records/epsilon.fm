import { expect, test } from '@playwright/test';

test('home page has expected text', async ({ page }) => {
	await page.goto('/');
	await expect(page.locator('text=Made with ❤️ by Epsilon Records')).toBeVisible();
});
