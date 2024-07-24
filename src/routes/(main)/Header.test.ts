import { describe, it, expect } from 'vitest';
import Header from './header.svelte';

describe('Header', () => {
	it('should render', () => {
		expect(Header).toBeTruthy();
	});
});
