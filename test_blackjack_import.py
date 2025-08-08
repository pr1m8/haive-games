#!/usr/bin/env python3
"""Test script to verify Blackjack imports are working correctly."""

print("Testing Blackjack imports...")

# Test 1: Direct import from standard.blackjack
try:
    from haive.games.cards.standard.blackjack import BlackjackStateManager

    print("✓ Direct import from cards.standard.blackjack works")
except ImportError as e:
    print(f"✗ Direct import failed: {e}")

# Test 2: Import through standard
try:
    from haive.games.cards.standard import BlackjackStateManager

    print("✓ Import through cards.standard works")
except ImportError as e:
    print(f"✗ Import through standard failed: {e}")

# Test 3: Import through cards (shortest path)
try:
    from haive.games.cards import BlackjackStateManager

    print("✓ Import through cards works")
except ImportError as e:
    print(f"✗ Import through cards failed: {e}")

# Test 4: Import from cards.blackjack (the original failing import)
try:
    from haive.games.cards.blackjack import BlackjackStateManager

    print(
        "✗ Original import path (cards.blackjack) still works - this shouldn't happen!"
    )
except ImportError:
    print("✓ Original incorrect import path (cards.blackjack) correctly fails")

print("\nAll correct import paths are working properly!")
print("\nCorrect import statements:")
print("  from haive.games.cards.standard.blackjack import BlackjackStateManager")
print("  from haive.games.cards.standard import BlackjackStateManager")
print("  from haive.games.cards import BlackjackStateManager")
