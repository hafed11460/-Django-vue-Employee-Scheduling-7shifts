export function tokenAlive(exp) {
    if (Date.now() >= exp * 1000) {
      return false;
    }
    return true;
  }